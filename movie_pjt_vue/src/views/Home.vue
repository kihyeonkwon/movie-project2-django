<template>
  <div class="home">
    <!-- Carousel wrapper -->
    <div
      id="carouselDarkVariant"
      class="carousel slide carousel-fade carousel-dark"
      data-mdb-ride="carousel"
    >
      <!-- Indicators -->
      <div class="carousel-indicators">
        <button
          data-mdb-target="#carouselDarkVariant"
          data-mdb-slide-to="0"
          class="active"
          aria-current="true"
          aria-label="Slide 1"
        ></button>
        <button
          data-mdb-target="#carouselDarkVariant"
          data-mdb-slide-to="1"
          aria-label="Slide 1"
        ></button>
        <button
          data-mdb-target="#carouselDarkVariant"
          data-mdb-slide-to="2"
          aria-label="Slide 1"
        ></button>
      </div>

      <!-- Inner -->
      <div class="carousel-inner">
        <!-- Single item -->
        <div class="carousel-item active">
          <img
            src="https://mdbootstrap.com/img/Photos/Slides/img%20(19).jpg"
            class="d-block w-100"
            alt="..."
          />
          <div class="carousel-caption d-none d-md-block">
            <h5>First slide label</h5>
            <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
          </div>
        </div>

        <!-- Single item -->
        <div class="carousel-item">
          <img
            src="https://mdbootstrap.com/img/Photos/Slides/img%20(35).jpg"
            class="d-block w-100"
            alt="..."
          />
          <div class="carousel-caption d-none d-md-block">
            <h5>Second slide label</h5>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </div>
        </div>

        <!-- Single item -->
        <div class="carousel-item">
          <img
            src="https://mdbootstrap.com/img/Photos/Slides/img%20(40).jpg"
            class="d-block w-100"
            alt="..."
          />
          <div class="carousel-caption d-none d-md-block">
            <h5>Third slide label</h5>
            <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
          </div>
        </div>
      </div>
      <!-- Inner -->

      <!-- Controls -->
      <button
        class="carousel-control-prev"
        type="button"
        data-mdb-target="#carouselDarkVariant"
        data-mdb-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-mdb-target="#carouselDarkVariant"
        data-mdb-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <!-- Carousel wrapper -->

    <!-- movie wrapper -->
    <section class="list item-more" id="movieListExample1" style="padding-top: 0px;">
      <h2 class="section-title">인기 영화</h2>
      <div class="bx-wrapper" style="max-width: 1200px;">
        <div data-min="6" data-max="6" data-margin="18" data-pager="true" data-controls="true" data-noslide="true"
        class="bxslider bxslider-in" style="width: 20215% position: relative; transition-duration: 0s; transform: translated3d(0px, 0px, 0px);">
          <!-- movie image list 출력  -->
          <!-- single item -->
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias
export default {
  name: 'Home',
  components: {
  }
}
</script>
