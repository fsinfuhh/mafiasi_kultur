/* tslint:disable */
/* eslint-disable */
/**
 * Mafiasi Kulturgenießer API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import type {
  CastVoteRequest,
  MediumViewset,
} from '../models/index';
import {
    CastVoteRequestFromJSON,
    CastVoteRequestToJSON,
    MediumViewsetFromJSON,
    MediumViewsetToJSON,
} from '../models/index';

export interface MediumsCastVoteCreateRequest {
    id: string;
    castVoteRequest: CastVoteRequest;
}

export interface MediumsListRequest {
    ag?: string;
    unvotedOnly?: boolean;
}

export interface MediumsRetrieveRequest {
    id: string;
}

/**
 *
 */
export class MediumsApi extends runtime.BaseAPI {

    /**
     */
    async mediumsCastVoteCreateRaw(requestParameters: MediumsCastVoteCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<MediumViewset>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling mediumsCastVoteCreate.');
        }

        if (requestParameters.castVoteRequest === null || requestParameters.castVoteRequest === undefined) {
            throw new runtime.RequiredError('castVoteRequest','Required parameter requestParameters.castVoteRequest was null or undefined when calling mediumsCastVoteCreate.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/api/mediums/{id}/cast_vote/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: CastVoteRequestToJSON(requestParameters.castVoteRequest),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => MediumViewsetFromJSON(jsonValue));
    }

    /**
     */
    async mediumsCastVoteCreate(requestParameters: MediumsCastVoteCreateRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<MediumViewset> {
        const response = await this.mediumsCastVoteCreateRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     */
    async mediumsListRaw(requestParameters: MediumsListRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Array<MediumViewset>>> {
        const queryParameters: any = {};

        if (requestParameters.ag !== undefined) {
            queryParameters['ag'] = requestParameters.ag;
        }

        if (requestParameters.unvotedOnly !== undefined) {
            queryParameters['unvoted_only'] = requestParameters.unvotedOnly;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/api/mediums/`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(MediumViewsetFromJSON));
    }

    /**
     */
    async mediumsList(requestParameters: MediumsListRequest = {}, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Array<MediumViewset>> {
        const response = await this.mediumsListRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     */
    async mediumsRetrieveRaw(requestParameters: MediumsRetrieveRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<MediumViewset>> {
        if (requestParameters.id === null || requestParameters.id === undefined) {
            throw new runtime.RequiredError('id','Required parameter requestParameters.id was null or undefined when calling mediumsRetrieve.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/api/mediums/{id}/`.replace(`{${"id"}}`, encodeURIComponent(String(requestParameters.id))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => MediumViewsetFromJSON(jsonValue));
    }

    /**
     */
    async mediumsRetrieve(requestParameters: MediumsRetrieveRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<MediumViewset> {
        const response = await this.mediumsRetrieveRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
