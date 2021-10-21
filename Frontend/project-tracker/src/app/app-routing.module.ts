
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { ProjectPageComponent } from './project-page/project-page.component';
import { StudentProfileComponent } from './student-profile/student-profile.component';
import { AuthGuard } from './auth.guard';
import { UploadprojectComponent } from './uploadproject/uploadproject.component';
import { ProfileComponent } from './profile/profile.component';
import { CohortsComponent } from './cohorts/cohorts.component';
import { StylesComponent } from './styles/styles.component';

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'home', component: HomeComponent },
  { path: 'projects', component: ProjectPageComponent },
  { path: 'add-projects', component:UploadprojectComponent },
  { path: 'profile', component:StudentProfileComponent,canActivate:[AuthGuard] },
  { path: 'profiles', component:ProfileComponent },
  { path: 'cohorts', component:CohortsComponent },
  { path: 'styles', component:StylesComponent },
];


@NgModule({
  declarations: [],
  imports: [
    CommonModule,

    RouterModule.forRoot(routes, { useHash: true })

  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }

