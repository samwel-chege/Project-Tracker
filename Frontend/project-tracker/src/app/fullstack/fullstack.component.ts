import { Component, OnInit } from '@angular/core';
import { FullstackService } from '../services/fullstack.service';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-fullstack',
  templateUrl: './fullstack.component.html',
  styleUrls: ['./fullstack.component.css']
})
export class FullstackComponent implements OnInit {

  projects: any;
  constructor(private FService: FullstackService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.FullstackProjects();
  }

  FullstackProjects() {
    this.FService.getFullstackProjects().subscribe(projects => {
      this.projects = projects;
      console.log(this.projects);
    })
  }

}




