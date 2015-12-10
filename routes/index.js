var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Sebulba' } );
});

router.get('/control', function (req, res, next) {
  res.render('control', { title: 'CONTROL Sebulba'} );
});

module.exports = router;
