function calculateOtherLosses (extractLoss, heuft1Loss, heuft2Loss) {
  var otherLoss = extractLoss - heuft1Loss - heuft2Loss;
  console.log(extractLoss);
  return otherLoss;
}
