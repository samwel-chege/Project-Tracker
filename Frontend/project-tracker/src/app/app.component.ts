import { Component, OnInit } from '@angular/core';
import { ProjectService } from './services/project.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'project-tracker';

  constructor(private _ProjectService: ProjectService){

  }
  ngOnInit(){
    this.getProjects();
    this.new_project ={};
    this.user = {
      username: '',
      password: '',

    };
  }
}


