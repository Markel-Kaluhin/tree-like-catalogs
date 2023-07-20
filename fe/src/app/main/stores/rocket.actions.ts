import { createAction, props } from '@ngrx/store';

import { GeneralError } from '../../shared/model/error/general';
import {RocketNodeModel, RocketPropertyModel} from '../models/rocket.modell';

export const rocketActionTypes = {
  getTree: '[Rocket/API] Get Tree',
  getTreeSuccess: '[Rocket/API] Get Tree Success',
  getTreeFailed: '[Rocket/API] Get Tree Failed',
  createNode: '[Rocket/API] Create Node',
  createNodeSuccess: '[Rocket/API] Create Node Success',
  createNodeFailed: '[Rocket/API] Create Node Failed',
  deleteNode: '[Rocket/API] Delete Node',
  deleteNodeSuccess: '[Rocket/API] Delete Node Success',
  deleteNodeFailed: '[Rocket/API] Delete Node Failed',
  deleteProperty: '[Rocket/API] Delete Property',
  deletePropertySuccess: '[Rocket/API] Delete Property Success',
  deletePropertyFailed: '[Rocket/API] Delete Property Failed',
};

export const getTree = createAction(rocketActionTypes.getTree, props<{ path: string }>());

export const getTreeSuccess = createAction(rocketActionTypes.createNodeSuccess, props<{ rocket: RocketNodeModel }>());

export const getTreeFailed = createAction(rocketActionTypes.getTreeFailed, props<{ error: GeneralError }>());

export const createNode = createAction(rocketActionTypes.createNode, props<{ path: string, rocketProperty?: RocketPropertyModel }>());

export const createNodeSuccess = createAction(rocketActionTypes.createNodeSuccess, props<{ rocket: RocketNodeModel }>());

export const createNodeFailed = createAction(rocketActionTypes.createNodeFailed, props<{ error: GeneralError }>());

export const deleteNode = createAction(rocketActionTypes.deleteNode, props<{ nodeId: number}>());

export const deleteNodeSuccess = createAction(rocketActionTypes.deleteNodeSuccess, props<{ success: boolean }>());

export const deleteNodeFailed = createAction(rocketActionTypes.deleteNodeFailed, props<{ error: GeneralError }>());

export const deleteProperty = createAction(rocketActionTypes.deleteProperty, props<{ propertyId: number}>());

export const deletePropertySuccess = createAction(rocketActionTypes.deletePropertySuccess, props<{ success: boolean }>());

export const deletePropertyFailed = createAction(rocketActionTypes.deletePropertyFailed, props<{ error: GeneralError }>());
