# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True, editable = False
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db import connection






class DimConselho(models.Model):
    idconselho = models.AutoField(primary_key=True)
    nmconselho = models.CharField(max_length=50, blank=True, null=True)
    descconselho = models.CharField(max_length=50, blank=True, null=True)
    numregistro = models.CharField(max_length=10, blank=True, null=True)
    nmestado = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idconselho), self.nmconselho)
    #def __str__(self):
    #    return self.nmconselho
    
    class Meta:
        managed = True
        db_table = 'dim_conselho'


class DimConsulta(models.Model):
    idconsulta = models.AutoField(primary_key=True)
    dim_motivo_idmotivo = models.ForeignKey('DimMotivo', models.DO_NOTHING, db_column='dim_motivo_idmotivo')
    dim_medico_dim_especialidade_idespecialidade = models.IntegerField(editable=False)
    dim_medico_dim_conselho_idconselho = models.IntegerField(editable=False)
    dim_medico_idmedico = models.ForeignKey('DimMedico', models.DO_NOTHING, db_column='dim_medico_idmedico')
    dim_medico_dim_prestador_idprestador = models.IntegerField(editable=False)
    dim_medico_dim_tipo_funcionario_idtipo_funcionario = models.IntegerField(editable=False)
    dim_medico_dim_tipo_funcionario_dim_funcao_idfuncao = models.IntegerField(editable=False)
    nmconsulta = models.CharField(max_length=50, blank=True, null=True)
    dtconsulta = models.DateField(blank=True, null=True,editable=False)
    dim_exames = models.CharField(max_length=50, blank=True, null=True)
    qtdexames = models.IntegerField(blank=True, null=True)
    anammese = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idconsulta), self.nmconsulta)
    #def __str__(self):
    #    return self.nmconsulta
    def save(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('call insert_consulta(%s,%s,%s,%s,%s,%s);',
                            [str(self.dim_motivo_idmotivo).split(' ')[0],
                             str(self.dim_medico_idmedico).split(' ')[0],
                             str(self.nmconsulta),
                             str(self.dim_exames),
                             str(self.qtdexames),
                             str(self.anammese)])
    class Meta:
        managed = True
        db_table = 'dim_consulta'
        unique_together = (('idconsulta', 
                            'dim_motivo_idmotivo', 
                            'dim_medico_dim_especialidade_idespecialidade', 
                            'dim_medico_dim_conselho_idconselho', 
                            'dim_medico_idmedico', 
                            'dim_medico_dim_prestador_idprestador', 
                            'dim_medico_dim_tipo_funcionario_idtipo_funcionario', 
                            'dim_medico_dim_tipo_funcionario_dim_funcao_idfuncao'),)
class DimEndereco(models.Model):
    idendereco = models.AutoField(primary_key=True)
    nmendereco = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=5, blank=True, null=True)
    nmbairro = models.CharField(max_length=30, blank=True, null=True)
    nmcidade = models.CharField(max_length=30, blank=True, null=True)
    nmestado = models.CharField(max_length=2, blank=True, null=True)
    nmpais = models.CharField(max_length=30, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)
    nmcomplento = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idendereco), self.nmendereco)

    class Meta:
        managed = True
        db_table = 'dim_endereco'


class DimEnderecoCep(models.Model):
    idendereco_cep = models.AutoField(primary_key=True)
    nmcep = models.CharField(max_length=30, blank=True, null=True)
    nm_enereco = models.CharField(max_length=5, blank=True, null=True)
    nmbairro = models.CharField(max_length=30, blank=True, null=True)
    nmcidade = models.CharField(max_length=30, blank=True, null=True)
    nmestado = models.CharField(max_length=2, blank=True, null=True)
    nmobservacao = models.CharField(max_length=80, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idendereco_cep), self.nmcep)

    
    class Meta:
        managed = True
        db_table = 'dim_endereco_cep'


class DimEspecialidade(models.Model):
    idespecialidade = models.AutoField(primary_key=True)
    nmespecialidade = models.CharField(max_length=20, blank=True, null=True)
    nmdescricao = models.CharField(max_length=20, blank=True, null=True)
    observacao = models.CharField(max_length=20, blank=True, null=True)
    dtregistro = models.DateField(blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idespecialidade), self.nmespecialidade)
    class Meta:
        managed = True
        db_table = 'dim_especialidade'


class DimExames(models.Model):
    idexames = models.AutoField(primary_key=True)
    dtexame = models.DateField(blank=True, null=True)
    dtcoleta = models.DateField(blank=True, null=True)
    dtresultado = models.DateField(blank=True, null=True)
    nmexame = models.CharField(max_length=50, blank=True, null=True)
    nmobservacao = models.CharField(max_length=50, blank=True, null=True)
    idconsulta = models.IntegerField()
    def __str__(self):
        return '%s %s' % (str(self.idexames), self.nmexame)
    class Meta:
        managed = True
        db_table = 'dim_exames'


class DimFuncao(models.Model):
    idfuncao = models.AutoField(primary_key=True)
    nmcargo = models.CharField(max_length=20, blank=True, null=True)
    dtcadastro = models.DateField(blank=True, null=True)
    nmobservacao = models.CharField(max_length=20, blank=True, null=True)
    num_cat_trabalho = models.CharField(max_length=20, blank=True, null=True)
    serie = models.CharField(max_length=20, blank=True, null=True)
    num_pis_pasep = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idfuncao), self.nmcargo)
    class Meta:
        managed = True
        db_table = 'dim_funcao'


class DimMedico(models.Model):
    idmedico = models.AutoField(primary_key=True)
    dim_prestador_idprestador = models.ForeignKey('DimPrestador', models.DO_NOTHING, db_column='dim_prestador_idprestador')
    dim_tipo_funcionario_idtipo_funcionario = models.ForeignKey('DimTipoFuncionario', models.DO_NOTHING, db_column='dim_tipo_funcionario_idtipo_funcionario')
    dim_conselho_idconselho = models.ForeignKey('DimConselho', models.DO_NOTHING, db_column='dim_conselho_idconselho')
    dim_especialidade_idespecialidade = models.ForeignKey('DimEspecialidade', models.DO_NOTHING, db_column='dim_especialidade_idespecialidade')
    dim_tipo_funcionario_dim_funcao_idfuncao = models.IntegerField()
    dtcadastro = models.DateField(blank=True, null=True,editable=False)
    observacao = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idmedico), str(self.dim_prestador_idprestador))
    class Meta:
        managed = True
        db_table = 'dim_medico'
        unique_together = (('idmedico', 'dim_prestador_idprestador', 'dim_tipo_funcionario_idtipo_funcionario', 'dim_conselho_idconselho', 'dim_especialidade_idespecialidade', 'dim_tipo_funcionario_dim_funcao_idfuncao'),)
    def save(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('call insert_medico(%s,%s,%s,%s,%s);',
                            [str(self.dim_prestador_idprestador).split(' ')[0],
                             str(self.dim_tipo_funcionario_idtipo_funcionario).split(' ')[0],
                             str(self.dim_conselho_idconselho).split(' ')[0],
                             str(self.dim_especialidade_idespecialidade).split(' ')[0],
                             str(self.observacao)])

class DimMotivo(models.Model):
    idmotivo = models.AutoField(primary_key=True)
    nmmotivo = models.CharField(max_length=20, blank=True, null=True)
    nmobservacao = models.CharField(max_length=20, blank=True, null=True)
    dtmotivo = models.DateField(blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idmotivo), self.nmmotivo)
    class Meta:
        managed = True
        db_table = 'dim_motivo'


class DimPessoa(models.Model):
    idpessoa = models.AutoField(primary_key=True)
    dim_endereco_cep_idendereco_cep = models.ForeignKey('DimEnderecoCep', models.DO_NOTHING, db_column='dim_endereco_cep_idendereco_cep')
    dim_tipo_pessoa_idtipo_pessoa = models.ForeignKey('DimTipoPessoa', models.DO_NOTHING, db_column='dim_tipo_pessoa_idtipo_pessoa')
    nmpessoa = models.CharField(max_length=50, blank=True, null=True)
    dtcadastro = models.DateField(blank=True, null=True)
    nmobservacao = models.CharField(max_length=50, blank=True, null=True)
    nm_numero = models.CharField(max_length=50, blank=True, null=True)
    nmcomplemento = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idpessoa), self.nmpessoa)
    class Meta:
        managed = True
        db_table = 'dim_pessoa'
        unique_together = (('idpessoa', 'dim_endereco_cep_idendereco_cep', 'dim_tipo_pessoa_idtipo_pessoa'),)


class DimPrestador(models.Model):
    idprestador = models.AutoField(primary_key=True)
    nmprestador = models.CharField(max_length=20, blank=True, null=True)
    dtcadastro = models.DateField(blank=True, null=True)
    nmobservacao = models.CharField(max_length=20, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    dtregistro = models.DateField(blank=True, null=True)
    nmjunta_comercial = models.CharField(max_length=20, blank=True, null=True)
    nmestado = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idprestador), self.nmprestador)
    class Meta:
        managed = True
        db_table = 'dim_prestador'


class DimTipoFuncionario(models.Model):
    idtipo_funcionario = models.AutoField(primary_key=True)
    dim_funcao_idfuncao = models.ForeignKey(DimFuncao, models.DO_NOTHING, db_column='dim_funcao_idfuncao')
    nmtipo_funcionario = models.CharField(max_length=20, blank=True, null=True)
    dtregistro = models.DateField(blank=True, null=True)
    dtcontratacao = models.DateField(blank=True, null=True)
    nmclassificacao = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idtipo_funcionario), self.nmtipo_funcionario)
    class Meta:
        managed = True
        db_table = 'dim_tipo_funcionario'
        unique_together = (('idtipo_funcionario', 'dim_funcao_idfuncao'),)


class DimTipoPessoa(models.Model):
    idtipo_pessoa = models.AutoField(primary_key=True)
    nmpfisica = models.CharField(max_length=25, blank=True, null=True)
    nmpjuridica = models.CharField(max_length=25, blank=True, null=True)
    dtcadastro = models.DateField(blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idtipo_pessoa), str(self.nmcep)+str(self.nmpjuridica))
    class Meta:
        managed = True
        db_table = 'dim_tipo_pessoa'





class FatoAtendimento(models.Model):
    idatendimento = models.AutoField(primary_key=True)
    dim_endereco_idendereco = models.ForeignKey('DimEndereco', models.DO_NOTHING, db_column='dim_endereco_idendereco')
    dim_consulta_idconsulta = models.ForeignKey('DimConsulta', models.DO_NOTHING, db_column='dim_consulta_idconsulta')
    dim_pessoa_idpessoa = models.ForeignKey('DimPessoa', models.DO_NOTHING, db_column='dim_pessoa_idpessoa')
    dim_tipo_funcionario_idtipo_funcionario = models.ForeignKey('DimTipoFuncionario', models.DO_NOTHING, db_column='dim_tipo_funcionario_idtipo_funcionario')
    dim_tipo_funcionario_dim_funcao_idfuncao = models.IntegerField(editable=False)
    dim_consulta_dim_medico_dim_tipo_funcionario_dim_funcao_idfunca = models.IntegerField(editable=False)
    dim_consulta_dim_medico_dim_tipo_funcionario_idtipo_funcionario = models.IntegerField(editable=False)
    dim_consulta_dim_medico_dim_prestador_idprestador = models.IntegerField(editable=False)
    dim_consulta_dim_medico_idmedico = models.IntegerField(editable=False)
    dim_consulta_dim_medico_dim_conselho_idconselho = models.IntegerField(editable=False)
    dim_consulta_dim_medico_dim_especialidade_idespecialidade = models.IntegerField(editable=False)
    dim_consulta_dim_motivo_idmotivo = models.IntegerField(editable=False)
    dim_pessoa_dim_tipo_pessoa_idtipo_pessoa = models.IntegerField(editable=False)
    dim_pessoa_dim_endereco_cep_idendereco_cep = models.IntegerField(editable=False)
    idconsulta = models.IntegerField(blank=True, null=True,editable=False)
    idpaciente = models.IntegerField(blank=True, null=True,editable=False)
    dtatendimento = models.DateField(blank=True, null=True,editable=False)
    idatendente = models.IntegerField(blank=True, null=True, editable=False)
    nmatendimento = models.CharField(max_length=32, blank=True, null=True)
    def __str__(self):
        return '%s %s' % (str(self.idatendente), self.nmatendimento)
    class Meta:
        managed = True
        db_table = 'fato_atendimento'
        unique_together = (('idatendimento', 'dim_endereco_idendereco', 'dim_consulta_idconsulta', 'dim_pessoa_idpessoa', 'dim_tipo_funcionario_idtipo_funcionario', 'dim_tipo_funcionario_dim_funcao_idfuncao', 'dim_consulta_dim_medico_dim_tipo_funcionario_dim_funcao_idfunca', 'dim_consulta_dim_medico_dim_tipo_funcionario_idtipo_funcionario', 'dim_consulta_dim_medico_dim_prestador_idprestador', 'dim_consulta_dim_medico_idmedico', 'dim_consulta_dim_medico_dim_conselho_idconselho', 'dim_consulta_dim_medico_dim_especialidade_idespecialidade', 'dim_consulta_dim_motivo_idmotivo', 'dim_pessoa_dim_tipo_pessoa_idtipo_pessoa', 'dim_pessoa_dim_endereco_cep_idendereco_cep'),)
    def save(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute('call insert_atendimento(%s,%s,%s,%s,%s);',
                            [str(self.dim_endereco_idendereco).split(' ')[0],
                             str(self.dim_pessoa_idpessoa).split(' ')[0],
                             str(self.dim_tipo_funcionario_idtipo_funcionario).split(' ')[0],
                             str(self.dim_consulta_idconsulta).split(' ')[0],
                             str(self.nmatendimento)])
        


