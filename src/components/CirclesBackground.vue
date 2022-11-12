<template>
    <div class="background">

        <svg>
            <linearGradient id="my_gradient" x1="50%" y1="0%" x2="50%" y2="100%" >
                <stop offset="0%" stop-color="#DB00FF">
                    <animate attributeName="stop-color" values="#DB00FF; #06D2FF; #DB00FF" dur="4s" repeatCount="indefinite"></animate>
                </stop>
                <stop offset="100%" stop-color="#06D2FF">
                    <animate attributeName="stop-color" values="#06D2FF; #DB00FF; #06D2FF" dur="4s" repeatCount="indefinite"></animate>
                </stop>
            </linearGradient>
        </svg>
        <svg style="left: 1%; top: 40%" width="8vw" height="8vw" class="movement1">
            <circle cx="4vw" cy="4vw" r="4vw" class="background_animated-gradient" />
        </svg>

        <svg style="left: 5%; top: 10%" width="6vw" height="6vw" class="movement2">
            <circle cx="3vw" cy="3vw" r="3vw" class="background_animated-gradient" />
        </svg>

        <svg style="left: 7%; top: 75%" width="4vw" height="4vw" class="movement3">
            <circle cx="2vw" cy="2vw" r="2vw" class="background_animated-gradient" />
        </svg>

        <svg style="left: 13%; top: 87% " width="6vw" height="6vw" class="movement4">
            <circle cx="3vw" cy="3vw" r="3vw" class="background_animated-gradient" />
        </svg>

        <svg style="left: 29.5%; top: 1.8% " width="6vw" height="6vw" class="movement5">
            <circle cx="3vw" cy="3vw" r="3vw" class="background_animated-gradient" />
        </svg>

        <svg style="left: 34.3%; top: 55% " width="8vw" height="8vw" class="movement6">
            <circle cx="4vw" cy="4vw" r="4vw" class="background_animated-gradient" />
        </svg>

        <svg style="left: 55%; top: 1% " width="4vw" height="4vw" class="movement1">
            <circle cx="2vw" cy="2vw" r="2vw" class="background_animated-gradient" />
        </svg>

        <svg style="left: 53%; top: 86% " width="6vw" height="6vw" class="movement2">
            <circle cx="3vw" cy="3vw" r="3vw" class="background_animated-gradient" />
        </svg>

        <svg style="left: 75%; top:0.5% " width="8vw" height="8vw" class="movement3">
            <circle cx="4vw" cy="4vw" r="4vw" class="background_animated-gradient" />
        </svg>

        <svg style="right: 1%; top: 87% " width="6vw" height="6vw" class="movement4">
            <circle cx="3vw" cy="3vw" r="3vw" class="background_animated-gradient" />
        </svg>

        <svg style="right: 8%; top: 50%" width="8vw" height="8vw" class="movement5">
            <circle cx="4vw" cy="4vw" r="4vw" class="background_animated-gradient" />
        </svg>

        <svg style="right: 2%; top: 13%" width="4vw" height="4vw" class="movement6">
            <circle cx="2vw" cy="2vw" r="2vw" class="background_animated-gradient" />
        </svg>

    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'CirclesBackground'
})
</script>

<style scoped lang="scss">
@import '../assets/variables.scss';

@function randomNum($min, $max) {
  $rand: random();
  $randomNum: $min + floor($rand * (($max - $min) + 1));

  @return $randomNum;
}
.movement1 {
    @extend %common-movement-animation;
    animation-duration: #{randomNum(10, 16)}s;
    animation-delay: #{randomNum(0, 2)};
}
.movement2 {
    @extend %common-movement-animation;
    animation-duration: #{randomNum(10, 16)}s;
    animation-delay: #{randomNum(0, 2)};
}
.movement3 {
    @extend %common-movement-animation;
    animation-duration: #{randomNum(6, 10)}s;
    animation-delay: #{randomNum(0, 2)};
}
.movement4 {
    @extend %common-movement-animation;
    animation-duration: #{randomNum(10, 16)}s;
    animation-delay: #{randomNum(0, 2)};
}
.movement5 {
    @extend %common-movement-animation;
    animation-duration: #{randomNum(10, 16)}s;
    animation-delay: #{randomNum(0, 2)};
}
.movement6 {
    @extend %common-movement-animation;
    animation-duration: #{randomNum(10, 16)}s;
    animation-delay: #{randomNum(0, 2)};
}

@keyframes move {
    0% {transform: translateX(0) translateY(0)}
    20% {transform: translateX(#{randomNum(-20, 20)}px) translateY(#{randomNum(-20, 20)}px)}
    40% {transform: translateX(#{randomNum(-10, 10)}px) translateY(#{randomNum(-10, 10)}px)}
    60% {transform: translateX(#{randomNum(-20, 20)}px) translateY(#{randomNum(-20, 20)}px)}
    80% {transform: translateX(#{randomNum(-10, 10)}px) translateY(#{randomNum(-10, 10)}px)}
    100% {transform: translateX(0) translateY(0)}
}
.background {
    position: absolute;
    display: block;
    width: 100%;
    max-width: 3840px;
    height: 100%;
    background-color: transparent;
}
.background_animated-gradient{
    fill: url('#my_gradient');
}

svg {
  display: flex;
  position: absolute;
  transform: rotate(-45deg);
}

/* Отключить для мобильной версии */
@media only screen
  and (min-device-width: 320px)
  and (max-device-width: 640px)
  and (-webkit-min-device-pixel-ratio: 2)
{
    .background{
        display: none;
    }
}
</style>
