/* tslint:disable */
/* eslint-disable */
/**
 * NLP Sandbox Deidentifier API
 * The OpenAPI specification implemented by NLP Sandbox PHI Deidentifiers. # Overview TBA 
 *
 * The version of the OpenAPI document: 0.3.1
 * Contact: thomas.schaffter@sagebionetworks.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * Configuration for the masking char strategy. E.g. "John Smith lives at 123 Main St" -> "********* lives at ***********".
 * @export
 * @interface DeidentificationConfigDeidentificationStrategyMaskingCharConfig
 */
export interface DeidentificationConfigDeidentificationStrategyMaskingCharConfig {
    /**
     * Character used to mask annotated PII text.
     * @type {string}
     * @memberof DeidentificationConfigDeidentificationStrategyMaskingCharConfig
     */
    maskingChar?: string;
}

export function DeidentificationConfigDeidentificationStrategyMaskingCharConfigFromJSON(json: any): DeidentificationConfigDeidentificationStrategyMaskingCharConfig {
    return DeidentificationConfigDeidentificationStrategyMaskingCharConfigFromJSONTyped(json, false);
}

export function DeidentificationConfigDeidentificationStrategyMaskingCharConfigFromJSONTyped(json: any, ignoreDiscriminator: boolean): DeidentificationConfigDeidentificationStrategyMaskingCharConfig {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'maskingChar': !exists(json, 'maskingChar') ? undefined : json['maskingChar'],
    };
}

export function DeidentificationConfigDeidentificationStrategyMaskingCharConfigToJSON(value?: DeidentificationConfigDeidentificationStrategyMaskingCharConfig | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'maskingChar': value.maskingChar,
    };
}


