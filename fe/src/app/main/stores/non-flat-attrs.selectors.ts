import { createFeatureSelector, createSelector } from '@ngrx/store';

import * as fromStoreNonFlatAttrs from './non-flat-attrs.reducers';
import { NonFlatAttrsNodeModel } from '../models/non-flat-attrs.modell';

const selectNonFlatAttrsNode = createFeatureSelector<NonFlatAttrsNodeModel>(fromStoreNonFlatAttrs.featureKey);

export const nonFlatAttrsNode = createSelector(selectNonFlatAttrsNode, (state: NonFlatAttrsNodeModel) => state);
