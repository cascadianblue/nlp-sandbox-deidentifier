/* tslint:disable */
/* eslint-disable */
/**
 * NLP Sandbox Deidentifier API
 * The OpenAPI specification implemented by NLP Sandbox PHI Deidentifiers. # Overview TBA 
 *
 * The version of the OpenAPI document: 0.2.2
 * Contact: thomas.schaffter@sagebionetworks.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * A clinical note
 * @export
 * @interface Note
 */
export interface Note {
    /**
     * The ID of the note
     * @type {string}
     * @memberof Note
     */
    readonly id?: string;
    /**
     * The content of the clinical note
     * @type {string}
     * @memberof Note
     */
    text: string;
    /**
     * The note type (LOINC concept)
     * @type {string}
     * @memberof Note
     */
    noteType: string;
    /**
     * The patient ID
     * @type {string}
     * @memberof Note
     */
    patientId?: string;
}

export function NoteFromJSON(json: any): Note {
    return NoteFromJSONTyped(json, false);
}

export function NoteFromJSONTyped(json: any, ignoreDiscriminator: boolean): Note {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'text': json['text'],
        'noteType': json['noteType'],
        'patientId': !exists(json, 'patientId') ? undefined : json['patientId'],
    };
}

export function NoteToJSON(value?: Note | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'text': value.text,
        'noteType': value.noteType,
        'patientId': value.patientId,
    };
}


