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
import {
    AnnotationSource,
    AnnotationSourceFromJSON,
    AnnotationSourceFromJSONTyped,
    AnnotationSourceToJSON,
    TextDateAnnotation,
    TextDateAnnotationFromJSON,
    TextDateAnnotationFromJSONTyped,
    TextDateAnnotationToJSON,
    TextPersonNameAnnotation,
    TextPersonNameAnnotationFromJSON,
    TextPersonNameAnnotationFromJSONTyped,
    TextPersonNameAnnotationToJSON,
    TextPhysicalAddressAnnotation,
    TextPhysicalAddressAnnotationFromJSON,
    TextPhysicalAddressAnnotationFromJSONTyped,
    TextPhysicalAddressAnnotationToJSON,
} from './';

/**
 * An annotation record
 * @export
 * @interface Annotation
 */
export interface Annotation {
    /**
     * Resource name of the annotation record, of the form datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId}
     * @type {string}
     * @memberof Annotation
     */
    readonly name?: string;
    /**
     * 
     * @type {AnnotationSource}
     * @memberof Annotation
     */
    annotationSource?: AnnotationSource;
    /**
     * Date annotations in a text
     * @type {Array<TextDateAnnotation>}
     * @memberof Annotation
     */
    textDateAnnotations?: Array<TextDateAnnotation>;
    /**
     * Person name annotations in a text
     * @type {Array<TextPersonNameAnnotation>}
     * @memberof Annotation
     */
    textPersonNameAnnotations?: Array<TextPersonNameAnnotation>;
    /**
     * Physical address annotations in a text
     * @type {Array<TextPhysicalAddressAnnotation>}
     * @memberof Annotation
     */
    textPhysicalAddressAnnotations?: Array<TextPhysicalAddressAnnotation>;
}

export function AnnotationFromJSON(json: any): Annotation {
    return AnnotationFromJSONTyped(json, false);
}

export function AnnotationFromJSONTyped(json: any, ignoreDiscriminator: boolean): Annotation {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': !exists(json, 'name') ? undefined : json['name'],
        'annotationSource': !exists(json, 'annotationSource') ? undefined : AnnotationSourceFromJSON(json['annotationSource']),
        'textDateAnnotations': !exists(json, 'textDateAnnotations') ? undefined : ((json['textDateAnnotations'] as Array<any>).map(TextDateAnnotationFromJSON)),
        'textPersonNameAnnotations': !exists(json, 'textPersonNameAnnotations') ? undefined : ((json['textPersonNameAnnotations'] as Array<any>).map(TextPersonNameAnnotationFromJSON)),
        'textPhysicalAddressAnnotations': !exists(json, 'textPhysicalAddressAnnotations') ? undefined : ((json['textPhysicalAddressAnnotations'] as Array<any>).map(TextPhysicalAddressAnnotationFromJSON)),
    };
}

export function AnnotationToJSON(value?: Annotation | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'annotationSource': AnnotationSourceToJSON(value.annotationSource),
        'textDateAnnotations': value.textDateAnnotations === undefined ? undefined : ((value.textDateAnnotations as Array<any>).map(TextDateAnnotationToJSON)),
        'textPersonNameAnnotations': value.textPersonNameAnnotations === undefined ? undefined : ((value.textPersonNameAnnotations as Array<any>).map(TextPersonNameAnnotationToJSON)),
        'textPhysicalAddressAnnotations': value.textPhysicalAddressAnnotations === undefined ? undefined : ((value.textPhysicalAddressAnnotations as Array<any>).map(TextPhysicalAddressAnnotationToJSON)),
    };
}


