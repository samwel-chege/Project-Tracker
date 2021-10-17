import { HashLocationStrategy } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../services/project.service';
@Component({
  selector: 'app-project-page',
  templateUrl: './project-page.component.html',
  styleUrls: ['./project-page.component.css']
})
export class ProjectPageComponent implements OnInit {
  projects: any;
  constructor(private projectService: ProjectService) { }

  ngOnInit(): void {
    this.AllProjects();
  }
  AllProjects(){
    this.projectService.getprojects().subscribe(projects => {
      this.projects = projects;
      console.log(this.projects)
    })
  }

}
