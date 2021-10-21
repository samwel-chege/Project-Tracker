import { Component, OnInit } from '@angular/core';
import { CohortsService } from '../services/cohorts.service';

@Component({
  selector: 'app-cohorts',
  templateUrl: './cohorts.component.html',
  styleUrls: ['./cohorts.component.css']
})
export class CohortsComponent implements OnInit {

  cohorts: any;
  constructor(private CService: CohortsService) { }

  ngOnInit(): void {
    this.AllCohorts();
  }

  AllCohorts() {
    this.CService.getCohorts().subscribe(cohorts => {
      this.cohorts = cohorts;
      console.log(this.cohorts);
    })
  }

}

