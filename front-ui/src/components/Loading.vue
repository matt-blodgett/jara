<template>
  <div class="loader loader--style2">
    <q-inner-loading showing>
      <q-spinner size="5em" color="amber" />
    </q-inner-loading>
  </div>
</template>

<script>
export default {
  name: 'Loading'
}
</script>

<style scoped lang=stylus>
  .loader
    height 100px
    width 100%
    text-align center
    padding 1em
    margin 0 auto 1em
    display inline-block
    vertical-align top
  svg path
    fill #ffa035
</style>
