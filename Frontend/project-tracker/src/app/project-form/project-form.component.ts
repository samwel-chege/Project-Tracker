import { Component, OnInit } from '@angular/core';
import { NewProjectService } from '../services/new-project.service';

@Component({
  selector: 'app-project-form',
  templateUrl: './project-form.component.html',
  styleUrls: ['./project-form.component.css']
})
export class ProjectFormComponent implements OnInit {

  constructor(private newProjectService: NewProjectService) { }

  ngOnInit(): void {
    
  }

}
