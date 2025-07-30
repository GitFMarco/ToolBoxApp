"""HTML files templates"""


INDEX_TEMPLATE: str = """<!--
Copyright %s - Huroos srl - www.huroos.com
License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
Powered by %s
-->

<section class="oe_container lead bi_title_box">
    <div>
        <div>
            <h2 class="oe_slogan bi_title" style="color:#5082c4;">
                <img src="icon.png" style="width:60px"><b>%s</b>
            </h2>
            <p style="text-align:center;">
                %s
            </p>
        </div>
    </div>
</section>

<section class="oe_container lead mt64">
    <div>
        <div class="oe_slogan oe_spaced">
            <a  title="Email"
                href="mailto:info@huroos.com"
                target="_top"> Email us - info@huroos.com</a><br/>
            <a title="Contact us"
               href="https://www.huroos.com"
               target="_blank"> Web site - ww.huroos.com </a>
        </div>
    </div>
</section>
"""
