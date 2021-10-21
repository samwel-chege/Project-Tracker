import { Component, OnInit } from '@angular/core';
import { StylesService } from '../services/styles.service';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-styles',
  templateUrl: './styles.component.html',
  styleUrls: ['./styles.component.css']
})
export class StylesComponent implements OnInit {

  styles: any;
  constructor(private StService: StylesService, private router: Router, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.AllStyles();
  }

  AllStyles() {
    this.StService.getStyles().subscribe(styles => {
      this.styles = styles;
      console.log(this.styles);
    })
  }

  navigateToStyle(id) {
    this.router.navigate(['./' + id], {relativeTo: this.activatedRoute});
  }
}
