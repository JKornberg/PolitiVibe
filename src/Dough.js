import React, {Component} from 'react';
import {Doughnut} from 'react-chartjs-2';
class Dough extends Component{


  getDoughnutData(data, checked){

    const colors = checked ? ['#4ACF6B', '#C444DB']: ['#218BFF', '#EB4739']

    var res = {
      'datasets' : [
        {
          'backgroundColor' : colors,
          'data' : data
        }
      ],
    }
    if (checked){
      res['labels'] = ['Facts', 'Opinions']
    }else{
      res['labels'] = ['Positive Tweets', 'Negative Tweets']
    }
    return res;
  }


  render(){



    return(
      <Doughnut data = {this.getDoughnutData(this.props.data, this.props.checked)} options ={ {'maintainAspectRatio' : false, 'tooltips' : {'enabled' : true, 'backgroundColor' : 'rgba(0, 0, 0, 0.8)'}}}/>
    )}
}

export default Dough
