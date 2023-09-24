import { createAction, props } from '@ngrx/store';

import { GeneralError } from '../../shared/model/error/general';
import {NonFlatAttrsNodeModel, NonFlatAttrsPropertyModel} from '../models/non-flat-attrs.modell';

export const nonFlatAttrsActionTypes = {
  getTree: '[NonFlatAttrs/API] Get Tree',
  getTreeSuccess: '[NonFlatAttrs/API] Get Tree Success',
  getTreeFailed: '[NonFlatAttrs/API] Get Tree Failed',
  createNode: '[NonFlatAttrs/API] Create Node',
  createNodeSuccess: '[NonFlatAttrs/API] Create Node Success',
  createNodeFailed: '[NonFlatAttrs/API] Create Node Failed',
  deleteNode: '[NonFlatAttrs/API] Delete Node',
  deleteNodeSuccess: '[NonFlatAttrs/API] Delete Node Success',
  deleteNodeFailed: '[NonFlatAttrs/API] Delete Node Failed',
  deleteProperty: '[NonFlatAttrs/API] Delete Property',
  deletePropertySuccess: '[NonFlatAttrs/API] Delete Property Success',
  deletePropertyFailed: '[NonFlatAttrs/API] Delete Property Failed',
};

export const getTree = createAction(nonFlatAttrsActionTypes.getTree, props<{ path: string }>());

export const getTreeSuccess = createAction(nonFlatAttrsActionTypes.createNodeSuccess, props<{ nonFlatAttrs: NonFlatAttrsNodeModel }>());

export const getTreeFailed = createAction(nonFlatAttrsActionTypes.getTreeFailed, props<{ error: GeneralError }>());

export const createNode = createAction(nonFlatAttrsActionTypes.createNode, props<{ path: string, nonFlatAttrsProperty?: NonFlatAttrsPropertyModel }>());

export const createNodeSuccess = createAction(nonFlatAttrsActionTypes.createNodeSuccess, props<{ nonFlatAttrs: NonFlatAttrsNodeModel }>());

export const createNodeFailed = createAction(nonFlatAttrsActionTypes.createNodeFailed, props<{ error: GeneralError }>());

export const deleteNode = createAction(nonFlatAttrsActionTypes.deleteNode, props<{ nodeId: number}>());

export const deleteNodeSuccess = createAction(nonFlatAttrsActionTypes.deleteNodeSuccess, props<{ success: boolean }>());

export const deleteNodeFailed = createAction(nonFlatAttrsActionTypes.deleteNodeFailed, props<{ error: GeneralError }>());

export const deleteProperty = createAction(nonFlatAttrsActionTypes.deleteProperty, props<{ propertyId: number}>());

export const deletePropertySuccess = createAction(nonFlatAttrsActionTypes.deletePropertySuccess, props<{ success: boolean }>());

export const deletePropertyFailed = createAction(nonFlatAttrsActionTypes.deletePropertyFailed, props<{ error: GeneralError }>());
