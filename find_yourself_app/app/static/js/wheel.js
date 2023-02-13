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
      data: [['AFR', 'rs1229984', 1981.0, 1],
      ['AFR', 'rs4833103', 1945.0, 2],
      ['AFR', 'rs6754311', 1931.0, 3],
      ['AFR', 'rs2238151', 1918.0, 4],
      ['AFR', 'rs2196051', 1916.0, 5],
      ['AMR', 'rs1229984', 981.0, 1],
      ['AMR', 'rs1462906', 978.0, 2],
      ['AMR', 'rs3916235', 943.0, 3],
      ['AMR', 'rs7722456', 887.0, 4],
      ['AMR', 'rs4891825', 874.0, 5],
      ['EAS', 'rs6754311', 1512.0, 1],
      ['EAS', 'rs4833103', 1512.0, 2],
      ['EAS', 'rs2196051', 1511.0, 3],
      ['EAS', 'rs3916235', 1507.0, 4],
      ['EAS', 'rs4891825', 1504.0, 5],
      ['EUR', 'rs1462906', 1471.0, 1],
      ['EUR', 'rs1229984', 1464.0, 2],
      ['EUR', 'rs3916235', 1452.0, 3],
      ['EUR', 'rs7997709', 1419.0, 4],
      ['EUR', 'rs16891982', 1416.0, 5],
      ['SAS', 'rs4833103', 1450.0, 1],
      ['SAS', 'rs1229984', 1435.0, 2],
      ['SAS', 'rs1462906', 1408.0, 3],
      ['SAS', 'rs3916235', 1371.0, 4],
      ['SAS', 'rs7722456', 1320.0, 5]],
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