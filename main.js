var color = "#75A5B7";
var color_green = "#30C328";
var color_purple = "#7628A1";
var maxParticles = 21;

// tsParticles Config.
tsParticles.load("tsparticles", {
  fpsLimit: 60,
  particles: {
    number: {
      value: maxParticles,
      density: {
        enable: false,
        value_area: maxParticles * 100
      }
    },
    color: {
      value: [color, color_green, color_purple]
    },
    shape: {
      type: "circle",
      stroke: {
        width: 0,
        color: "#000000"
      },
      polygon: {
        nb_sides: 5
      }
    },
    opacity: {
      value: 0.5,
      random: false,
      anim: {
        enable: false,
        speed: 1,
        opacity_min: 0.1,
        sync: false
      }
    },
    size: {
      value: 3,
      random: true,
      anim: {
        enable: false,
        speed: 40,
        size_min: 0.1,
        sync: false
      }
    },
    line_linked: {
      enable: true,
      distance: 50,
      color: "random",
      blink: false,
      consent: false,
      opacity: 1,
      width: 8, 
    },
    move: {
      enable: true,
      speed: 5,
      direction: "bottom-left", 
      random: false,
      straight: false,
      out_mode: "out",
      bounce: false,
      attract: {
        enable: true,
        rotateX: 600,
        rotateY: 1200
      }
    }
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: {
        enable: true,
        mode: "grab"
      },
      onclick: {
        enable: true,
        mode: "push"
      },
      resize: true
    },
    modes: {
      grab: {
        distance: 150,
        line_linked: {
          opacity: 1,
          color: "#537665", // use average color until 'grab' is able to find the particle color. https://github.com/matteobruni/tsparticles/issues/669
        },
      },
      bubble: {
        distance: 400,
        size: 40,
        duration: 2,
        opacity: 8,
        speed: 3
      },
      repulse: {
        distance: 200,
        duration: 0.4
      },
      push: {
        particles_nb: 4
      },
      remove: {
        particles_nb: 2
      }
    }
  },
  retina_detect: true
});
