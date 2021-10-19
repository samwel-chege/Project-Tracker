import { Component, OnInit } from '@angular/core';
import { StylesService } from '../services/styles.service';

@Component({
  selector: 'app-styles',
  templateUrl: './styles.component.html',
  styleUrls: ['./styles.component.css']
})
export class StylesComponent implements OnInit {

  styles: any;
  constructor(private StService: StylesService) { }

  ngOnInit(): void {
    this.AllStyles();
  }

  AllStyles() {
    this.StService.getStyles().subscribe(styles => {
      this.styles = styles;
      console.log(this.styles);
    })
  }

}
