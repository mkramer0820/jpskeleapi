import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { CustomerListComponent } from './customer-list/customer-list.component';
import { CustomerCreateComponent } from './customer-create/customer-create.component';
import { FactoryListComponent } from './factory-list/factory-list.component';
import { FactoryCreateComponent } from './factory-create/factory-create.component';
import { OrderListComponent } from './order-list/order-list.component';
import { OrderCreateComponent } from './order-create/order-create.component';
import { TaskListComponent } from './task-list/task-list.component';
import { TaskCreateComponent } from './task-create/task-create.component';

import { AppRoutingModule } from './app-routing.module';

import { HttpClientModule , HttpClientXsrfModule } from '@angular/common/http';





@NgModule({
  declarations: [
    AppComponent,
    CustomerListComponent,
    CustomerCreateComponent,
    FactoryListComponent,
    FactoryCreateComponent,
    OrderListComponent,
    OrderCreateComponent,
    TaskListComponent,
    TaskCreateComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName : 'csrftoken',
      headerName : 'X-CSRFToken'
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
