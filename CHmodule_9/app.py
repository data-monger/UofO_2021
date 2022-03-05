
import datetime as dt
import numpy as np 
import pandas as pd 
import sqlalchemy as sqlA

from sqlalchemy.ext.automap import automap_base as autB
from sqlalchemy.orm import Session as session
from sqlalchemy import create_engine as engC, func

from flask import Flask as flsk
from flask import jsonify as jsnC

engine = engC('sqlite:///hawaii.sqlite')
base_ = autB()
base_.prepare(engine, reflect=True)

measure_f=base_.classes.measurement
station_f=base_.classes.station

#sess = session(engine)
appF = flsk(__name__)



##########
@appF.route('/')
def welcome():
    return (
        '''
        Welcome to the Climate Analysis API.    <br>
        Available Routes:                       <br>
        /api/v1.0/precipitation                 <br>
        /api/v1.0/stations                      <br>
        /api/v1.0/tobs                          <br>
        /api/v1.0/temp/start/end                <br>
        '''
    )

@appF.route('/api/v1.0/precipitation')
def precipitation():
    sess = session(engine)
    prev_yr = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precip_qr = sess.query(measure_f.date, measure_f.prcp).filter(measure_f.date >= prev_yr).all()
    precip_ls = {date: prcp for date, prcp in precip_qr}
    sess.close()
    return jsnC(precip_ls=precip_ls)


@appF.route('/api/v1.0/stations')
def stations():
    sess= session(engine)
    result = sess.query(station_f.station).all()
    station_ls = list(np.ravel(result))
    sess.close()
    return jsnC(station_ls=station_ls)


@appF.route('/api/v1.0/tobs')
def tobs():
    sess= session(engine)
    prev_yr = dt.date(2017,8,23) - dt.timedelta(days=365)
    result_qy = sess.query(measure_f.tobs).filter(measure_f.station == 'USC00519281').filter(measure_f.date >= prev_yr).all()
    temps_ls = list(np.ravel(result_qy))
    sess.close()
    return jsnC(temps_ls=temps_ls)


@appF.route('/api/v1.0/temp/<start>')
@appF.route('/api/v1.0/temp/<start>/<end>')
def stats(start=None, end=None):
    sess=session(engine)
    sel_ls = [func.min(measure_f.tobs), func.avg(measure_f.tobs), func.max(measure_f.tobs)]

    if not end:
        result_qy=sess.query(*sel_ls).filter(measure_f.date >= start).all()
        temp_ls = list(np.ravel(result_qy))
        sess.close()
        return jsnC(temp_ls=temp_ls)
 
    result_qy= sess.query(*sel_ls).filter(measure_f.date >=start).filter(measure_f.date <=end).all()
    temp_ls = list(np.ravel(result_qy))
    sess.close()
    return jsnC(temp_ls=temp_ls)
    

