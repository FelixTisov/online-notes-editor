<template>
    <div class="background">

        <svg>
            <linearGradient id="my-gradient" x1="50%" y1="0%" x2="50%" y2="100%" > 
                <stop offset="0%" stop-color="#DB00FF">
                    <animate attributeName="stop-color" values="#DB00FF; #06D2FF; #DB00FF" dur="4s" repeatCount="indefinite"></animate>
                </stop>
                <stop offset="100%" stop-color="#06D2FF">
                    <animate attributeName="stop-color" values="#06D2FF; #DB00FF; #06D2FF" dur="4s" repeatCount="indefinite"></animate>
                </stop>
            </linearGradient> 
        </svg>

        <!-- <svg style="left: 1%; top: 40%" width="132px" height="132px">
            <circle cx="66" cy="66" r="66" class="animated-gradient" />
        </svg>

            <svg style="left: 5%; top: 10%" width="90px" height="90px">
                <circle cx="45" cy="45" r="45" class="animated-gradient" />
            </svg>

            <svg style="left: 7%; top: 75%" width="54px" height="54px">
                <circle cx="27" cy="27" r="27" class="animated-gradient" />
            </svg>

        <svg style="left: 13%; top: 88% " width="84px" height="84px">
            <circle cx="42" cy="42" r="42" class="animated-gradient" />
        </svg>

        <svg style="left: 29.5%; top: 1.8% " width="90px" height="90px">
            <circle cx="45" cy="45" r="45" class="animated-gradient" />
        </svg>

        <svg style="left: 34.3%; top: 55% " width="8vw" height="8vw">
            <circle cx="4vw" cy="4vw" r="4vw" class="animated-gradient" />
        </svg>

        <svg style="left: 55%; top: 1% " width="54px" height="54px">
            <circle cx="27" cy="27" r="27" class="animated-gradient" />
        </svg>

        <svg style="left: 53%; top: 88% " width="84px" height="84px">
            <circle cx="42" cy="42" r="42" class="animated-gradient" />
        </svg>

        <svg style="left: 75%; top:0.5% " width="128px" height="128px">
            <circle cx="64" cy="64" r="64" class="animated-gradient" />
        </svg>

        <svg style="right: 1%; top: 87% " width="90px" height="90px">
            <circle cx="45" cy="45" r="45" class="animated-gradient" />
        </svg>

            <svg style="right: 8%; top: 50%" width="132px" height="132px">
                <circle cx="66" cy="66" r="66" class="animated-gradient" />
            </svg>

            <svg style="right: 2%; top: 13%" width="54px" height="54px">
                <circle cx="27" cy="27" r="27" class="animated-gradient" />
            </svg> -->

        
        <svg style="left: 1%; top: 40%" width="8vw" height="8vw">
            <circle cx="4vw" cy="4vw" r="4vw" class="animated-gradient" />
        </svg>

            <svg style="left: 5%; top: 10%" width="6vw" height="6vw">
                <circle cx="3vw" cy="3vw" r="3vw" class="animated-gradient" />
            </svg>

            <svg style="left: 7%; top: 75%" width="4vw" height="4vw">
                <circle cx="2vw" cy="2vw" r="2vw" class="animated-gradient" />
            </svg>

        <svg style="left: 13%; top: 87% " width="6vw" height="6vw">
            <circle cx="3vw" cy="3vw" r="3vw" class="animated-gradient" />
        </svg>

        <svg style="left: 29.5%; top: 1.8% " width="6vw" height="6vw">
            <circle cx="3vw" cy="3vw" r="3vw" class="animated-gradient" />
        </svg>

        <svg style="left: 34.3%; top: 55% " width="8vw" height="8vw">
            <circle cx="4vw" cy="4vw" r="4vw" class="animated-gradient" />
        </svg>

        <svg style="left: 55%; top: 1% " width="4vw" height="4vw">
            <circle cx="2vw" cy="2vw" r="2vw" class="animated-gradient" />
        </svg>

        <svg style="left: 53%; top: 86% " width="6vw" height="6vw">
            <circle cx="3vw" cy="3vw" r="3vw" class="animated-gradient" />
        </svg>

        <svg style="left: 75%; top:0.5% " width="8vw" height="8vw">
            <circle cx="4vw" cy="4vw" r="4vw" class="animated-gradient" />
        </svg>

        <svg style="right: 1%; top: 87% " width="6vw" height="6vw">
            <circle cx="3vw" cy="3vw" r="3vw" class="animated-gradient" />
        </svg>

            <svg style="right: 8%; top: 50%" width="8vw" height="8vw">
                <circle cx="4vw" cy="4vw" r="4vw" class="animated-gradient" />
            </svg>

            <svg style="right: 2%; top: 13%" width="4vw" height="4vw">
                <circle cx="2vw" cy="2vw" r="2vw" class="animated-gradient" />
            </svg>

    </div>
</template>

<script>
export default {
  name: 'CirclesBackground'
}
</script>

<style scoped>
.animated-gradient{
    fill: url('#my-gradient');
}

.background {
    position: absolute;
    display: block;
    width: 100%;
    max-width: 3840px;
    /* max-width: 1719px; */
    height: 100%;
    background-color: transparent;
}
svg {
  display: flex;
  position: absolute;
  transform: rotate(-45deg);
}
</style>