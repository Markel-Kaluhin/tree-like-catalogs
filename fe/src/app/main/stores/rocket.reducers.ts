import { Action, createReducer, on } from '@ngrx/store';

import { RocketNodeModel } from '../models/rocket.modell';
import * as RocketActions from './rocket.actions';

export const featureKey = 'rocket';

export const initialState: RocketNodeModel = <RocketNodeModel>{};

const rocketReducers = createReducer(
  initialState,
  on(RocketActions.getTreeSuccess, (state, action) => ({
    ...action.rocket,
  })),
  on(RocketActions.createNodeSuccess, (state, action) => ({
    ...action.rocket,
  })),
);

export function reducer(state: RocketNodeModel, action: Action) {
  return rocketReducers(state, action);
}
