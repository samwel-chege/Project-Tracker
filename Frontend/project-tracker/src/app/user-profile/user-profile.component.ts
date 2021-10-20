import { Component, OnInit } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { UserProfileService } from '../services/user-profile.service';
import { map, switchMap, tap } from 'rxjs/operators';
import { Inject } from '@angular/core';


@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})

export class UserProfileComponent {
  student: any;
//   id: any;
//   user: any;

//   private userId$: Observable<number> = this.activatedRoute.params.pipe(
//     map((params: Params) => parseInt(params['id']))
//   )

//   user$: Observable<any> = this.userId$.pipe(
//     switchMap((userId: number) => this.UPService.findOne(userId))
//   )

//   constructor(
//     private activatedRoute: ActivatedRoute,
//     private UPService: UserProfileService,
//   ) { }

//   userProfile() {
//     this.UPService.findOne(this.id).subscribe(user => {
//       this.user = user;
//       console.log(this.user);
//     })
//   }

constructor(private UPService: UserProfileService,  private router: Router, private route: ActivatedRoute) { }

ngOnInit(): void {
  this.Project();
}

Project(){
  this.UPService.getStudent('id').subscribe(student => {
    this.student = student;
    console.log(this.student)
  })
}
}