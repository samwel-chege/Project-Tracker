import { Proj } from './../../../models/proj';
import { ActivatedRoute, Router } from '@angular/router';
import { UploadprojectService } from './../services/uploadproject.service';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-uploadproject',
  templateUrl: './uploadproject.component.html',
  styleUrls: ['./uploadproject.component.css']
})
export class UploadprojectComponent implements OnInit {

    form!: FormGroup
    selectedFile: File;
    description: string;
    title: string
    link: string
    owner: string



  constructor(
    private UploadprojectService: UploadprojectService,
    private route: ActivatedRoute,
    private router: Router,
    private formBuilder: FormBuilder,

  ) { }
  imageUpload(event:any){
    this.selectedFile = event.target.files[0];
    console.log(this.selectedFile)
  }

  descriptionChange(event:any){
    this.description = event.target.value;
    console.log(this.description)
   }

   titleChange(event:any){
    this.title = event.target.value;
    console.log(this.title)
   }

   linkChange(event:any){
    this.link = event.target.value;
    console.log(this.link)
   }
   ownerChange(event:any){
    this.owner = event.target.value;
    console.log(this.owner)
   }

  ngOnInit(): void {
  }
  addProject(){
  const fd = new FormData();
  fd.append('project_image', this.selectedFile)
  fd.append('description', this.description)
  fd.append('title', this.title)
  fd.append('owner', this.owner)
  fd.append('github_link', this.link)
  this.UploadprojectService.uploadProject(fd).subscribe(data =>{
    console.log(data)
  })
  this.router.navigate(['projects'])
}
refresh(){
  window.location.reload();
}
}