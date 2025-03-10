import { APP_INITIALIZER, NgModule } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { MarkdownModule, MarkedOptions, MarkedRenderer } from 'ngx-markdown';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { AudioService } from './service/audio.service';
import { AutoEnableAudioService } from './service/auto-enable-audio.service';
import { BrowserModule } from '@angular/platform-browser';
import { DummyComponent } from './component/dummy/dummy.component';
import { EmulationService } from './service/emulation.service';
import { KvsService } from './service/kvs.service';
import { PageLockService } from './service/page-lock.service';
import { RouteReuseStrategy } from '@angular/router';
import { ServiceWorkerModule } from '@angular/service-worker';
import { SessionService } from 'src/app/service/session.service';
import { StorageService } from './service/storage.service';
import { UpdateService } from './service/update.service';
import { environment } from '../environments/environment';

const markedOptionsFactory = (): MarkedOptions => {
    const renderer = new MarkedRenderer();

    renderer.link = (href, title, text) => `<a href="${href}" target="_blank" rel="external">${text || href}</a>`;

    return {
        renderer,
        gfm: true,
        breaks: false,
        pedantic: false,
        smartLists: true,
        smartypants: false,
    };
};

@NgModule({
    declarations: [AppComponent, DummyComponent],
    imports: [
        BrowserModule,
        IonicModule.forRoot(),
        AppRoutingModule,
        ServiceWorkerModule.register('ngsw-worker.js', { enabled: environment.production }),
        MarkdownModule.forRoot({
            loader: HttpClient,
            markedOptions: { provide: MarkedOptions, useFactory: markedOptionsFactory },
        }),
        HttpClientModule,
    ],
    providers: [
        { provide: RouteReuseStrategy, useClass: IonicRouteStrategy },
        {
            provide: APP_INITIALIZER,
            multi: true,
            useFactory: (kvsService: KvsService) => kvsService.initialize.bind(kvsService),
            deps: [KvsService],
        },
    ],
    bootstrap: [AppComponent],
})
export class AppModule {
    constructor(
        pageLockService: PageLockService,
        storageService: StorageService,
        emulationService: EmulationService,
        audioService: AudioService,
        sessionService: SessionService,
        kvs: KvsService,
        updateService: UpdateService,
        autoEnableAudioService: AutoEnableAudioService
    ) {}
}
