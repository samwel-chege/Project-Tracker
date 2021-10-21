import { Component, OnInit } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { CohortService } from '../services/cohort.service';
import { map, switchMap, tap } from 'rxjs/operators';
import { Inject } from '@angular/core';

@Component({
  selector: 'app-cohort',
  templateUrl: './cohort.component.html',
  styleUrls: ['./cohort.component.css']
})
export class CohortProjectsComponent implements OnInit {
  projects: any;
  cohort: any;
  id: any;

  constructor(private CPService: CohortService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.Cohort();
  }

  Cohort(){
    this.CPService.getCohort(this.cohort.id).subscribe(projects => {
      this.projects = projects;
      console.log(this.projects)
    })
  }
}