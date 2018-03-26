import ir2_base as ir
import Motions as mo

ir.open_port()
ir.set_speed(300)
ir.set_sleep(0.3)

ir.nk(90)
ir.nk(40)
ir.nk(90)
ir.nk(130)
ir.nk(90)

ir.initall()

ir.set_sleep(0.3)
mo.Archit_motion()
ir.set_sleep(0.4)
mo.Mohak_motion()
mo.shashwat_motion()
mo.sandeep_motion()
ir.set_sleep(0.3)
mo.surya_motion()
mo.unknown_motion()

ir.initall()
ir.close_port()
