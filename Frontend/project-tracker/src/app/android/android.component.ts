import { Component, OnInit } from '@angular/core';
import { AndroidService } from '../services/android.service';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-android',
  templateUrl: './android.component.html',
  styleUrls: ['./android.component.css']
})
export class AndroidComponent implements OnInit {

  projects: any;
  constructor(private AService: AndroidService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.CohortProjects();
  }

  CohortProjects() {
    this.AService.getAndroidProjects().subscribe(projects => {
      this.projects = projects;
      console.log(this.projects);
    })
  }

}


