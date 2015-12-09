import gulp from 'gulp';


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
