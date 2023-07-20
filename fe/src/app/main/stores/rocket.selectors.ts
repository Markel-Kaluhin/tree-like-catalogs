import { createFeatureSelector, createSelector } from '@ngrx/store';

import * as fromStoreRocket from './rocket.reducers';
import { RocketNodeModel } from '../models/rocket.modell';

const selectRocketNode = createFeatureSelector<RocketNodeModel>(fromStoreRocket.featureKey);

export const rocketNode = createSelector(selectRocketNode, (state: RocketNodeModel) => state);
