import { Component, OnInit } from '@angular/core';
import { StudentProfileService } from '../services/student.service';
import { AuthService } from '../services/auth.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-student-profile',
  templateUrl: './student-profile.component.html',
  styleUrls: ['./student-profile.component.css']
})
export class StudentProfileComponent implements OnInit {


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
