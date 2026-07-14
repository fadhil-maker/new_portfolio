import { type SchemaTypeDefinition } from 'sanity'
import { profileType } from './profile'
import { educationType } from './education'
import { experienceType } from './experience'
import { projectType } from './project'
import { skillType } from './skill'
import { certificationType } from './certification'

export const schema: { types: SchemaTypeDefinition[] } = {
  types: [
    profileType,
    educationType,
    experienceType,
    projectType,
    skillType,
    certificationType,
  ],
}
