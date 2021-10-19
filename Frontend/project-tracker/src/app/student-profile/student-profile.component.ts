import { Component, OnInit } from '@angular/core';
import { StudentProfileService } from '../services/student.service';
import { ProjectService } from '../services/project.service';
import { AuthService } from '../services/auth.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-student-profile',
  templateUrl: './student-profile.component.html',
  styleUrls: ['./student-profile.component.css']
})
export class StudentProfileComponent implements OnInit {
  // currentUser: object = {};

  // constructor(
  //   public authService: AuthService,
  //   private actRoute: ActivatedRoute
  // ){
  //   let id = this.actRoute.snapshot.paramMap.get('id');
  //   this.authService.getUserProfile(id).subscribe(res=>{
  //     this.currentUser = res.msg;
  //   })
  // }
  // // students: any;
  // // constructor( private studentProfileService: StudentProfileService) { }

  // ngOnInit(): void {
  //   // this.AllProfiles();
  // }
  // // AllProfiles(){
  // //   this.studentProfileService.getprofiles().subscribe(students =>{
  // //     this.students = students;
  // //     console.log(this.students)
  // //   })

  // // }


  student: any;
  constructor( private studentProfileService: StudentProfileService) { }

  ngOnInit(): void {
    this.MyProfile();
  }
  MyProfile(){
    this.studentProfileService.getProfile().subscribe(student =>{
      this.student = student;
      console.log(this.student)
    })

  }
}
