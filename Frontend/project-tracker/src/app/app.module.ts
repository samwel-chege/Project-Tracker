import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ProjectService } from './services/project.service';
import { UserService } from './services/user.service';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { AppRoutingModule } from './app-routing.module'; 
import { HomeComponent } from './home/home.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { ProjectPageComponent } from './project-page/project-page.component';
import { ProjectFormComponent } from './project-form/project-form.component';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { StudentProfileComponent } from './student-profile/student-profile.component';
import { ProfileComponent } from './profile/profile.component';

import { HttpClientModule } from '@angular/common/http';
import { CohortsComponent } from './cohorts/cohorts.component';
import { StylesComponent } from './styles/styles.component';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    ProjectPageComponent,
    ProjectFormComponent,
    SignupComponent,
    LoginComponent,
    StudentProfileComponent,
    ProfileComponent,
    CohortsComponent,
    StylesComponent,
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,  
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
