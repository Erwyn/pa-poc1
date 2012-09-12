# Copyright (c) 2012 LE GOFF Vincent
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of the copyright holder nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


"""This file contains the DataConnector class, defined below."""

from model.functions import *

class DataConnector:
    
    """Class representing a data connector, a wrapper of a data access.
    
    The DataConnector is an abstrat class, which SHOULD NOT be
    instanciated, but inherited from the usable data connectors.
    Each data connector represents a way to access organized datas,
    as a SQL driver or alike.
    
    Method to define in the subclass:
        __init__(config) -- the constructor (only called at runtime)
        connect() -- connect (to) the data connector
        disconnect() -- close the connexion to the data connector
    
    For more informations, see the details of each method.
    
    """
    
    def __init__(self):
        """Initialize the data connector."""
        self.objects_tree = {}
        self.tables = {}
    
    def record_tables(self, classes):
        """Record the given classes.
        
        The parameter must be a list of classes. Each class must
        be a model.
        
        """
        for model in classes:
            self.record_model(model)
    
    def record_model(self, model):
        """Record the given model, a subclass of model.Model."""
        name = get_name(model)
        self.tables[name] = model
        self.objects_tree[name] = []
        return name