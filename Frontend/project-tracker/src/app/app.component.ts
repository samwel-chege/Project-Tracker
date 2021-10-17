import { Component } from '@angular/core';
import { ProjectService } from './services/project.service';
import { AuthService } from './_services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'project-tracker';

  constructor(private _ProjectService: ProjectService, private authService: AuthService){

  }
}


