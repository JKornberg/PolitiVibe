import React, {Component} from 'react';
import {Radar} from 'react-chartjs-2';
class Chart extends Component{

  getRadarData(data){
    const colors = ['rgba(5, 135, 147, .3)',
    'rgba(0, 174, 98, .3)',
    'rgba(244, 175, 58, .3)',
    'rgba(242, 76, 40, .3)',
    'rgba(193, 72, 193, .3)',]

    const sentimentData = data
    var d = []
    var radarData = {};
    radarData['labels'] = [];
    const topics = Object.keys(sentimentData[0].topics)
    for (var topic of topics){
      if (topic !== "all"){
        radarData['labels'].push(topic)
      }
    }
    var datasets = []
    var counter = 0;
    for (var index in sentimentData){
      var dataArr = [];
      for (topic of topics){
        if (topic != "all"){
          dataArr.push((sentimentData[index]['topics'][topic]['polarity'] + 1)/2);
        }
      }
      datasets.push({
        "label" : sentimentData[index].info.name,
        "data" : dataArr,
        'backgroundColor' : colors[counter],
        'pointBackgroundColor' : colors[counter]
      });
      counter++;
      radarData['datasets'] = datasets;

    }
    return radarData;
  }

  render(){
    return (
      <Radar data = {this.getRadarData(this.props.data)} />
    )
  }
}

export default Chart
