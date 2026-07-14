import { getCliClient } from 'sanity/cli'
import { createReadStream } from 'fs'
import path from 'path'

// Dynamic import for the json file since it's commonjs and we are in module context or just use fs.readFileSync
import fs from 'fs'

const client = getCliClient()

async function uploadAsset(filePath: string, type: 'image' | 'file' = 'image') {
  try {
    const fullPath = path.join(process.cwd(), 'public', 'media', filePath)
    if (!fs.existsSync(fullPath)) {
      console.warn(`File not found: ${fullPath}`)
      return null
    }
    const asset = await client.assets.upload(type, createReadStream(fullPath), {
      filename: path.basename(filePath)
    })
    return {
      _type: 'image', // or file depending on usage, but usually Sanity image fields just want the reference
      asset: {
        _type: 'reference',
        _ref: asset._id
      }
    }
  } catch (err) {
    console.error(`Failed to upload ${filePath}:`, err)
    return null
  }
}

async function uploadFileAsset(filePath: string) {
  try {
    const fullPath = path.join(process.cwd(), 'public', 'media', filePath)
    if (!fs.existsSync(fullPath)) {
      console.warn(`File not found: ${fullPath}`)
      return null
    }
    const asset = await client.assets.upload('file', createReadStream(fullPath), {
      filename: path.basename(filePath)
    })
    return {
      _type: 'file',
      asset: {
        _type: 'reference',
        _ref: asset._id
      }
    }
  } catch (err) {
    console.error(`Failed to upload file ${filePath}:`, err)
    return null
  }
}

async function migrate() {
  console.log('Starting migration to Sanity...')
  const rawData = fs.readFileSync(path.join(process.cwd(), 'data.json'), 'utf8')
  // Fix BOM if exists
  const cleanData = rawData.charCodeAt(0) === 0xFEFF ? rawData.slice(1) : rawData
  const data = JSON.parse(cleanData)

  for (const item of data) {
    const model = item.model
    const pk = item.pk
    const fields = item.fields

    let docType = ''
    if (model === 'core.profile') docType = 'profile'
    else if (model === 'core.education') docType = 'education'
    else if (model === 'core.experience') docType = 'experience'
    else if (model === 'core.project') docType = 'project'
    else if (model === 'core.skill') docType = 'skill'
    else if (model === 'core.certification') docType = 'certification'
    else continue

    const _id = `${docType}-${pk}`
    console.log(`Migrating ${docType} (ID: ${_id})...`)

    const doc: any = {
      _id,
      _type: docType,
      ...fields
    }

    // Handle images and files
    if (docType === 'profile') {
      if (fields.profile_image) doc.profile_image = await uploadAsset(fields.profile_image)
      if (fields.resume_file) doc.resume_file = await uploadFileAsset(fields.resume_file)
    } else if (docType === 'experience') {
      if (fields.company_logo) doc.company_logo = await uploadAsset(fields.company_logo)
      if (fields.certificate_file) doc.certificate_file = await uploadFileAsset(fields.certificate_file)
    } else if (docType === 'project') {
      if (fields.image) doc.image = await uploadAsset(fields.image)
      if (fields.thumbnail) doc.thumbnail = await uploadAsset(fields.thumbnail)
    } else if (docType === 'certification') {
      if (fields.certificate_file) doc.certificate_file = await uploadFileAsset(fields.certificate_file)
    }

    // Clean up Django specific fields
    delete doc.created_at
    delete doc.updated_at
    delete doc.is_active

    await client.createOrReplace(doc)
    console.log(`Successfully migrated ${_id}`)
  }
  console.log('Migration complete!')
}

migrate().catch(console.error)
