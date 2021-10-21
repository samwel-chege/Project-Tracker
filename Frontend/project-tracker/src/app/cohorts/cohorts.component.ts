import { Component, OnInit } from '@angular/core';
import { CohortsService } from '../services/cohorts.service';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-cohorts',
  templateUrl: './cohorts.component.html',
  styleUrls: ['./cohorts.component.css']
})
export class CohortsComponent implements OnInit {

  cohorts: any;
  constructor(private CService: CohortsService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.AllCohorts();
  }

  AllCohorts() {
    this.CService.getCohorts().subscribe(cohorts => {
      this.cohorts = cohorts;
      console.log(this.cohorts);
    })
  }

  navigateToCohort(id) {
    console.clear();
    this.router.navigate(['./' + id], {relativeTo: this.activatedRoute});
  }

  navigateToAndroid() {
    console.clear();
    this.router.navigate(['./android'], {relativeTo: this.activatedRoute});
  }

  navigateToFullstack() {
    console.clear();
    this.router.navigate(['./fullstack'], {relativeTo: this.activatedRoute});
  }

}

