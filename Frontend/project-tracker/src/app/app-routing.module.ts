
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { ProjectPageComponent } from './project-page/project-page.component';
import { StudentProfileComponent } from './student-profile/student-profile.component';
import { ProjectFormComponent } from './project-form/project-form.component';
import { AuthGuard } from './auth.guard';
import { ProfileComponent } from './profile/profile.component';
import { CohortsComponent } from './cohorts/cohorts.component';
import { StylesComponent } from './styles/styles.component';
import { SingleProjectComponent } from './single-project/single-project.component';
import { UserProfileComponent } from './user-profile/user-profile.component';

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'home', component: HomeComponent },

  { path: 'projects',
    children: [
      { path: '', component: ProjectPageComponent },
      { path: ':id', component: SingleProjectComponent },
    ]
  },
  { path: 'profile', component:StudentProfileComponent,canActivate:[AuthGuard] },
  { path: 'add-projects', component:ProjectFormComponent },
  { path: 'profiles',
    children: [
      { path: '', component: ProfileComponent },
      { path: ':id', component: UserProfileComponent },
    ]
  },
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

