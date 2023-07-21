import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { MainComponent } from './main/component/main/main.component';
import * as fromRocket from './main/stores/rocket.reducers';
import {StoreModule} from "@ngrx/store";
import {EffectsModule} from "@ngrx/effects";
import {RocketEffects} from "./main/stores/rocket.effects";
import {HttpClientModule} from "@angular/common/http";
import {SharedModule} from "./shared/shared.module";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CreateNodeComponent } from './main/component/create-node/create-node.component';
import { CreatePropertyComponent } from './main/component/create-property/create-property.component';
import {ReactiveFormsModule} from "@angular/forms";
import {RelativeTimePipe} from "./shared/pipe/relative-time.pipe";

@NgModule({
    declarations: [
        MainComponent,
        CreateNodeComponent,
        CreatePropertyComponent,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        SharedModule,
        StoreModule.forRoot({}, {}),
        EffectsModule.forRoot([]),
        StoreModule.forFeature(fromRocket.featureKey, fromRocket.reducer),
        EffectsModule.forFeature([RocketEffects]),
        NgbModule,
        ReactiveFormsModule,
    ],
  providers: [RelativeTimePipe],
  bootstrap: [MainComponent]
})
export class AppModule { }
