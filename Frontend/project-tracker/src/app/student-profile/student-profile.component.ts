import { Component, OnInit } from '@angular/core';
import { StudentProfileService } from '../services/student.service';
import { ProjectService } from '../services/project.service';

@Component({
  selector: 'app-student-profile',
  templateUrl: './student-profile.component.html',
  styleUrls: ['./student-profile.component.css']
})
export class StudentProfileComponent implements OnInit {
  students: any;
  constructor( private studentProfileService: StudentProfileService) { }

  ngOnInit(): void {
    this.AllProfiles();
  }
  AllProfiles(){
    this.studentProfileService.getprofiles().subscribe(students =>{
      this.students = students;
      console.log(this.students)
    })

  }

}
