import babelify from 'babelify';
import browserify from 'browserify';
import domain from 'domain';
import gulp from 'gulp';
import gutil from 'gulp-util';
import hbsfy from 'hbsfy';
import plumber from 'gulp-plumber';
import tap from 'gulp-tap';


/* Default task */
gulp.task('default', function() {
  gulp.start('build');
});


/* Building all frontend assets */
gulp.task('build', function() {
  return gulp.src(['wysadzulice/assets/**/*',
    '!wysadzulice/assets/{plantingjs, plantingjs/**}'])
    .pipe(gulp.dest('./wysadzulice/static'));
});
/* End of building all frontend assets */


/* Building JS */
gulp.task('js', function() {
  return gulp.src('./node_modules/plantingjs/src/js/main.js')
    .pipe(plumber())
    .pipe(tap(function(file) {
      const dom = domain.create();
      dom.on('error', function(err) {
        gutil.log(
          gutil.colors.red('Browserify compile error:'),
          err.message, '\n\t',
          gutil.colors.cyan('in file'), file.path
        );
        gutil.beep();
      });
      dom.run(function() {
        file.contents = browserify({
          entries: [file.path],
          debug: true,
          standalone: 'Planting',
          paths: ['./node_modules', './src/js/'],
          transform: [hbsfy, babelify],
        }).bundle();
      });
    }))
    .pipe(gulp.dest('./wysadzulice/static/'));
});
/* End of building JS */
