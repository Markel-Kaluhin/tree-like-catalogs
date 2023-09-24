import { Action, createReducer, on } from '@ngrx/store';

import { NonFlatAttrsNodeModel } from '../models/non-flat-attrs.modell';
import * as NonFlatAttrsActions from './non-flat-attrs.actions';

export const featureKey = 'nonFlatAttrs';

export const initialState: NonFlatAttrsNodeModel = <NonFlatAttrsNodeModel>{};

const nonFlatAttrsReducers = createReducer(
  initialState,
  on(NonFlatAttrsActions.getTreeSuccess, (state, action) => ({
    ...action.nonFlatAttrs,
  })),
  on(NonFlatAttrsActions.createNodeSuccess, (state, action) => ({
    ...action.nonFlatAttrs,
  })),
);

export function reducer(state: NonFlatAttrsNodeModel, action: Action) {
  return nonFlatAttrsReducers(state, action);
}
