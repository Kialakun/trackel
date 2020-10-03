function calculateOtherLosses (extractLoss, heuft1Loss, heuft2Loss) {
  // calculate losses for the Loss Summary
  var otherLoss = extractLoss - heuft1Loss - heuft2Loss;
  return otherLoss;
}

function conditionalColoring (chart, target, time=false) {
  // conditional colring for charts
  var red = 'rgb(255, 0, 0, 0.5)';
  var redBorder = 'rgb(255, 0, 0, 1)';

  var datasets = chart.config.data.datasets;

  if (time) {
    for (var k in datasets) {
      for (var i in datasets[k].data) {
        if (datasets[k].data[i].y > target) {
          // change color of background and border to red
          datasets[k].backgroundColor[i] = red;
        }
      }
    }
  } else {
    for (var k in datasets) {
      for (var i in datasets[k].data) {
        if (datasets[k].data[i] > target) {
          // change color of background and border to red
          datasets[k].backgroundColor[i] = red;
        }
      }
    }
  }
  chart.update();

  console.log('conditional coloring');
  console.log(chart.config);

}
