console.log("wheel data:",wheel_data)
var datajson=wheel_data
console.log(datajson)
Highcharts.chart('container', {

    title: {
      text: 'Genomics Dependency Wheel'
    },
  
    accessibility: {
      point: {
        valueDescriptionFormat: '{index}. From {point.from} to {point.to}: {point.weight}.'
      }
    },
  
    series: [{
      keys: ['from', 'to', 'weight'],
      data: datajson,
      type: 'dependencywheel',
      name: 'Dependency wheel series',
      dataLabels: {
        color: '#333',
        style: {
          textOutline: 'none'
        },
        textPath: {
          enabled: true
        },
        distance: 10
      },
      size: '95%'
    }]
  
  });