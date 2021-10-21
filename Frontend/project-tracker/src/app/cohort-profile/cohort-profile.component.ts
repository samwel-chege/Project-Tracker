import { Component, OnInit } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { CohortProfileService } from '../services/cohort-profile.service';
import { map, switchMap, tap } from 'rxjs/operators';
import { Inject } from '@angular/core';

@Component({
  selector: 'app-cohort-profile',
  templateUrl: './cohort-profile.component.html',
  styleUrls: ['./cohort-profile.component.css']
})
export class CohortProfileComponent {
  cohort: any;

  private id$: Observable<number> = this.route.params.pipe(
    map((params: Params) => parseInt(params['id']))
  )

  cohort$: Observable<any> = this.id$.pipe(
    switchMap((id: number) => this.CPService.findOne(id))
  )

  constructor(private CPService: CohortProfileService,  private router: Router, private route: ActivatedRoute) { }

  // ngOnInit(): void {
  //   this.Cohort();
  // }

  // Cohort(){
  //   this.CPService.getCohort('id').subscribe(cohort => {
  //     this.cohort = cohort;
  //     console.log(this.cohort)
  //   })
  // }

  // filter(){
  //   console.clear();
  //   var filter_id = document.getElementById("filter").value;
  //   var filter_array = this.cohort.filter(x => x.id == filter_id);
  //   console.log(filter_array);
  // }
}